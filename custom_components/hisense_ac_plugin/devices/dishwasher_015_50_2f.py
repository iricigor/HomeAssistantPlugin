"""Parser for Hisense Dishwasher (015) device type with feature code 50.2f."""
from typing import Dict
from .base import BaseDeviceParser, DeviceAttribute

class Dishwasher015502FParser(BaseDeviceParser):
    """Parser for Hisense Dishwasher with type code 015 and feature code 50.2f."""
    
    @property
    def device_type(self) -> str:
        return "015"
        
    @property
    def feature_code(self) -> str:
        return "50.2f"
    
    @property
    def attributes(self) -> Dict[str, DeviceAttribute]:
        return {
            # Program/Status attributes - common dishwasher status keys
            "program": DeviceAttribute(
                key="program",
                name="Current Program",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Off",
                    "1": "Quick Wash",
                    "2": "Normal",
                    "3": "Intensive",
                    "4": "Eco",
                    "5": "Pre-wash",
                    "6": "Rinse",
                    "7": "Dry"
                },
                read_write="R"
            ),
            
            "state": DeviceAttribute(
                key="state",
                name="Dishwasher State",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Idle",
                    "1": "Running",
                    "2": "Paused",
                    "3": "Complete",
                    "4": "Error"
                },
                read_write="R"
            ),
            
            "remaining_time": DeviceAttribute(
                key="remaining_time",
                name="Remaining Time",
                attr_type="Number",
                step=1,
                value_range="0~300",  # 0-300 minutes
                read_write="R"
            ),
            
            "door": DeviceAttribute(
                key="door",
                name="Door Status",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Closed",
                    "1": "Open"
                },
                read_write="R"
            ),
            
            # Control attributes
            "power": DeviceAttribute(
                key="power",
                name="Power",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Off",
                    "1": "On"
                },
                read_write="RW"
            ),
            
            "selected_program": DeviceAttribute(
                key="selected_program",
                name="Selected Program",
                attr_type="Enum",
                step=1,
                value_map={
                    "1": "Quick Wash",
                    "2": "Normal",
                    "3": "Intensive",
                    "4": "Eco"
                },
                read_write="RW"
            ),
            
            # Temperature setting
            "temperature": DeviceAttribute(
                key="temperature",
                name="Water Temperature",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Cold",
                    "1": "40°C",
                    "2": "50°C",
                    "3": "60°C",
                    "4": "70°C"
                },
                read_write="RW"
            ),
            
            # Error code
            "error_code": DeviceAttribute(
                key="error_code",
                name="Error Code",
                attr_type="Number",
                step=1,
                value_range="0~99",
                read_write="R"
            ),
            
            # Water level/pressure
            "water_level": DeviceAttribute(
                key="water_level",
                name="Water Level",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Low",
                    "1": "Normal",
                    "2": "High"
                },
                read_write="R"
            ),
            
            # Rinse aid level
            "rinse_aid": DeviceAttribute(
                key="rinse_aid",
                name="Rinse Aid Level",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Empty",
                    "1": "Low",
                    "2": "Medium",
                    "3": "Full"
                },
                read_write="R"
            ),
            
            # Salt level
            "salt_level": DeviceAttribute(
                key="salt_level",
                name="Salt Level",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Empty",
                    "1": "Low",
                    "2": "Medium",
                    "3": "Full"
                },
                read_write="R"
            ),
            
            # Additional options
            "extra_rinse": DeviceAttribute(
                key="extra_rinse",
                name="Extra Rinse",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Off",
                    "1": "On"
                },
                read_write="RW"
            ),
            
            "delay_start": DeviceAttribute(
                key="delay_start",
                name="Delay Start (Hours)",
                attr_type="Number",
                step=1,
                value_range="0~24",
                read_write="RW"
            )
        }
