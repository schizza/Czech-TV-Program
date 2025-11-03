"""API client for Czech TV Program."""
import logging
import aiohttp
import asyncio
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from typing import Any, Dict, List

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import API_BASE_URL, API_TIMEOUT, AVAILABLE_CHANNELS, DEFAULT_DAYS_AHEAD

_LOGGER = logging.getLogger(__name__)


class CzTVProgramAPI:
    """API client for Czech TV Program."""

    def __init__(self, hass: HomeAssistant, username: str, channels: List[str]):
        """Initialize the API client."""
        self.hass = hass
        self.username = username
        self.channels = channels or list(AVAILABLE_CHANNELS.keys())
        self.session = async_get_clientsession(hass)
        
    async def async_update_data(self) -> Dict[str, Any]:
        """Fetch data from API endpoint."""
        try:
            all_data = {}
            
            for channel_id in self.channels:
                channel_data = await self._fetch_channel_program(channel_id)
                all_data[channel_id] = channel_data
                
            return all_data
            
        except Exception as err:
            _LOGGER.error("Error fetching TV program: %s", err)
            raise
    
    async def _fetch_channel_program(self, channel_id: str) -> List[Dict[str, Any]]:
        """Fetch program for a specific channel."""
        all_programs = []
        
        # Fetch program for next 7 days
        for day_offset in range(DEFAULT_DAYS_AHEAD):
            date = datetime.now() + timedelta(days=day_offset)
            date_str = date.strftime("%d.%m.%Y")
            
            url = f"{API_BASE_URL}?user={self.username}&date={date_str}&channel={channel_id}"
            
            try:
                async with self.session.get(url, timeout=API_TIMEOUT) as response:
                    if response.status == 200:
                        content = await response.text()
                        programs = self._parse_xml(content, date)
                        all_programs.extend(programs)
                    else:
                        _LOGGER.warning(
                            "Failed to fetch program for %s on %s: HTTP %s",
                            channel_id, date_str, response.status
                        )
                        
            except asyncio.TimeoutError:
                _LOGGER.error("Timeout fetching program for %s on %s", channel_id, date_str)
            except Exception as err:
                _LOGGER.error("Error fetching program for %s on %s: %s", channel_id, date_str, err)
                
            # Pause between requests to respect rate limiting
            await asyncio.sleep(1)
            
        return all_programs
    
    def _parse_xml(self, xml_content: str, date: datetime) -> List[Dict[str, Any]]:
        """Parse XML response."""
        programs = []
        
        try:
            root = ET.fromstring(xml_content)
            
            for porad in root.findall('porad'):
                program = {}
                
                # Time
                cas = porad.find('cas')
                if cas is not None:
                    program['time'] = cas.text
                    
                # Date
                datum = porad.find('datum')
                if datum is not None:
                    program['date'] = datum.text
                else:
                    program['date'] = date.strftime("%Y-%m-%d")
                
                # Titles
                nazvy = porad.find('nazvy')
                if nazvy is not None:
                    nadtitul = nazvy.find('nadtitul')
                    nazev = nazvy.find('nazev')
                    nazev_casti = nazvy.find('nazev_casti')
                    
                    program['supertitle'] = nadtitul.text if nadtitul is not None else ""
                    program['title'] = nazev.text if nazev is not None else "Bez názvu"
                    program['episode_title'] = nazev_casti.text if nazev_casti is not None else ""
                
                # Episode info
                dil = porad.find('dil')
                program['episode'] = dil.text if dil is not None and dil.text else ""
                
                # Genre
                zanr = porad.find('zanr')
                program['genre'] = zanr.text if zanr is not None else ""
                
                # Duration
                stopaz = porad.find('stopaz')
                program['duration'] = stopaz.text if stopaz is not None else ""
                
                # Description
                noticka = porad.find('noticka')
                program['description'] = noticka.text if noticka is not None else ""
                
                # Links
                linky = porad.find('linky')
                if linky is not None:
                    program_link = linky.find('program')
                    program['link'] = program_link.text if program_link is not None else ""
                else:
                    program['link'] = ""
                
                # Icons/attributes
                ikony = porad.find('ikony')
                if ikony is not None:
                    program['audio'] = ikony.find('zvuk').text if ikony.find('zvuk') is not None else ""
                    program['subtitles'] = ikony.find('skryte_titulky').text == "1" if ikony.find('skryte_titulky') is not None else False
                    program['live'] = ikony.find('live').text == "1" if ikony.find('live') is not None else False
                    program['premiere'] = ikony.find('premiera').text == "1" if ikony.find('premiera') is not None else False
                    program['aspect_ratio'] = ikony.find('pomer').text if ikony.find('pomer') is not None else ""
                
                programs.append(program)
                
        except ET.ParseError as err:
            _LOGGER.error("Error parsing XML: %s", err)
            
        return programs
