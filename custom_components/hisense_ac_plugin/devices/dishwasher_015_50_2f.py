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
            # Program/Status attributes - mapped to actual ConnectLife API keys
            "Current_program_phase": DeviceAttribute(
                key="Current_program_phase",
                name="Current Program Phase",
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
            
            "Door_status": DeviceAttribute(
                key="Door_status",
                name="Door Status",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Closed",
                    "1": "Open"
                },
                read_write="R"
            ),
            
            "Remaining_time": DeviceAttribute(
                key="Remaining_time",
                name="Remaining Time",
                attr_type="Number",
                step=1,
                value_range="0~300",  # 0-300 minutes
                read_write="R"
            ),
            
            "Machine_state": DeviceAttribute(
                key="Machine_state",
                name="Machine State",
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
            
            # Control attributes
            "Power_state": DeviceAttribute(
                key="Power_state",
                name="Power State",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Off",
                    "1": "On"
                },
                read_write="RW"
            ),
            
            "Selected_program": DeviceAttribute(
                key="Selected_program",
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
            "Water_temperature": DeviceAttribute(
                key="Water_temperature",
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
            "Error_code": DeviceAttribute(
                key="Error_code",
                name="Error Code",
                attr_type="Number",
                step=1,
                value_range="0~99",
                read_write="R"
            ),
            
            # Water level/pressure
            "Water_level": DeviceAttribute(
                key="Water_level",
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
            "Rinse_aid_level": DeviceAttribute(
                key="Rinse_aid_level",
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
            "Salt_level": DeviceAttribute(
                key="Salt_level",
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
            "Extra_rinse": DeviceAttribute(
                key="Extra_rinse",
                name="Extra Rinse",
                attr_type="Enum",
                step=1,
                value_map={
                    "0": "Off",
                    "1": "On"
                },
                read_write="RW"
            ),
            
            "Delay_start_hours": DeviceAttribute(
                key="Delay_start_hours",
                name="Delay Start (Hours)",
                attr_type="Number",
                step=1,
                value_range="0~24",
                read_write="RW"
            )
            
            # Commented out attributes with no direct mapping yet:
            # These would need to be mapped once we have the actual API dump
            
            # "Cycle_count": DeviceAttribute(
            #     key="Cycle_count",
            #     name="Cycle Count",
            #     attr_type="Number",
            #     step=1,
            #     value_range="0~9999",
            #     read_write="R"
            # ),
            
            # "Filter_status": DeviceAttribute(
            #     key="Filter_status",
            #     name="Filter Status",
            #     attr_type="Enum",
            #     step=1,
            #     value_map={
            #         "0": "Clean",
            #         "1": "Needs Cleaning",
            #         "2": "Blocked"
            #     },
            #     read_write="R"
            # )
        }
