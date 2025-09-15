"""Device parsers package."""
from typing import Dict, Type
import logging

from .atw_035_699 import SplitWater035699Parser
from .base import BaseDeviceParser
from .base_bean import BaseBeanParser
from .dishwasher_015_50_2f import Dishwasher015502FParser
from .hum_007 import Humidity007Parser
from .split_ac_009_199 import SplitAC009199Parser
from .window_ac_008_399 import WindowAC008399Parser
from .bean_006_299 import Split006299Parser
from .wash_m_025 import HisenseWashingMachineParser

_LOGGER = logging.getLogger(__name__)

# Registry of device parsers
DEVICE_PARSERS: Dict[tuple[str, str], Type[BaseDeviceParser]] = {
    ("035", "699"): SplitWater035699Parser,
    ("006", "299"): Split006299Parser,
    ("007", ""): Humidity007Parser,
    ("015", "50.2f"): Dishwasher015502FParser,
    ("025", ""): HisenseWashingMachineParser,
}

def get_device_parser(device_type: str, feature_code: str) -> Type[BaseDeviceParser]:
    """Get device parser for the given device type and feature code."""
    _LOGGER.debug("Getting device parser for type %s, feature_code %s", device_type, feature_code)
    
    # Check for exact parser match first
    parser_key = (device_type, feature_code)
    if parser_key in DEVICE_PARSERS:
        parser_class = DEVICE_PARSERS[parser_key]
        _LOGGER.info("Found specific parser for device type %s, feature_code %s: %s", 
                    device_type, feature_code, parser_class.__name__)
        return parser_class
    
    # Special case: Dishwasher 015 with feature code 50.2f - ensure it's always detected
    if device_type == "015" and feature_code == "50.2f":
        _LOGGER.info("Explicitly returning Dishwasher015502FParser for type 015, feature_code 50.2f")
        return Dishwasher015502FParser
    
    # Legacy handling for humidity devices
    if device_type == "007":
        _LOGGER.debug("除湿机设备 %s", device_type)
        return Humidity007Parser
    
    # Supported device types that can use the default parser
    supported_device_types = ["009", "008", "006", "015", "016", "025"]
    if device_type in supported_device_types:
        _LOGGER.debug("Using default BaseBeanParser for supported device type %s", device_type)
        return BaseBeanParser
    else:
        _LOGGER.warning("Unsupported device type: %s", device_type)
        raise ValueError(f"Unsupported device type: {device_type}")
