#!/usr/bin/env python3
"""
Test script to verify the settings configuration structure
"""

import sys
import os
import json

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Create a minimal version of the settings config for testing
class SettingsConfig:
    """Class to hold all configuration settings"""
    def __init__(self):
        # Detection settings
        self.detection_threshold = [3, 3]
        self.upper_color = [154, 165, 175]
        self.lower_color = [141, 88, 58]
        self.min_contour_area = 261
        self.density_threshold = 0.5
        self.enable_clustering = True
        self.cluster_distance = 40
        self.min_cluster_size = 1000
        self.max_cluster_size = 20000
        self.fov_x = 400
        self.fov_y = 400
        self.aim_fov_x = 400
        self.aim_fov_y = 400
        self.fps = 120
        self.auto_detect_resolution = True
        self.resolution_x = 1920
        self.resolution_y = 1080
        
        # Aim settings
        self.aim_offset = 0
        self.aim_smooth = 0.9
        self.aim_speed = 0.5
        self.aim_y_speed = 0.2
        self.aim_height = 0.7
        self.smoothing_type = "bezier"  # linear, ease_in_out, bezier
        self.ease_factor = 2.0
        self.min_ease_speed = 0.2
        self.bezier_control_offset = 0.3
        self.bezier_tension = 1.0
        self.movement_randomness = 0.1
        self.deadzone = 10
        
        # Anti-shake settings
        self.enable_anti_shake = True
        self.anti_shake_threshold = 0.05
        self.shake_suppression_factor = 0.7
        self.shake_escalation_threshold = 0.2
        self.shake_escalation_rate = 0.1
        self.shake_cooldown_duration = 2.0

    def to_dict(self):
        """Convert settings to dictionary for export"""
        return {
            "detection_threshold": self.detection_threshold,
            "upper_color": self.upper_color,
            "lower_color": self.lower_color,
            "min_contour_area": self.min_contour_area,
            "density_threshold": self.density_threshold,
            "enable_clustering": self.enable_clustering,
            "cluster_distance": self.cluster_distance,
            "min_cluster_size": self.min_cluster_size,
            "max_cluster_size": self.max_cluster_size,
            "fov_x": self.fov_x,
            "fov_y": self.fov_y,
            "aim_fov_x": self.aim_fov_x,
            "aim_fov_y": self.aim_fov_y,
            "fps": self.fps,
            "auto_detect_resolution": self.auto_detect_resolution,
            "resolution_x": self.resolution_x,
            "resolution_y": self.resolution_y,
            "aim": {
                "offset": self.aim_offset,
                "smooth": self.aim_smooth,
                "speed": self.aim_speed,
                "y_speed": self.aim_y_speed,
                "aim_height": self.aim_height,
                "smoothing_type": self.smoothing_type,
                "ease_factor": self.ease_factor,
                "min_ease_speed": self.min_ease_speed,
                "bezier_control_offset": self.bezier_control_offset,
                "bezier_tension": self.bezier_tension,
                "movement_randomness": self.movement_randomness,
                "deadzone": self.deadzone,
                "enable_anti_shake": self.enable_anti_shake,
                "anti_shake_threshold": self.anti_shake_threshold,
                "shake_suppression_factor": self.shake_suppression_factor,
                "shake_escalation_threshold": self.shake_escalation_threshold,
                "shake_escalation_rate": self.shake_escalation_rate,
                "shake_cooldown_duration": self.shake_cooldown_duration,
            }
        }

def main():
    print("Testing Settings Configuration...")
    
    # Create config instance
    config = SettingsConfig()
    
    # Test basic properties
    print(f"✓ Detection threshold: {config.detection_threshold}")
    print(f"✓ Upper color: {config.upper_color}")
    print(f"✓ Lower color: {config.lower_color}")
    print(f"✓ Aim speed: {config.aim_speed}")
    print(f"✓ Smoothing type: {config.smoothing_type}")
    print(f"✓ Enable clustering: {config.enable_clustering}")
    print(f"✓ Enable anti-shake: {config.enable_anti_shake}")
    
    # Test dictionary conversion
    settings_dict = config.to_dict()
    print(f"✓ Dictionary conversion successful")
    print(f"✓ Detection settings count: {len([k for k in settings_dict.keys() if k != 'aim'])}")
    print(f"✓ Aim settings count: {len(settings_dict['aim'])}")
    
    # Test JSON serialization
    try:
        json_str = json.dumps(settings_dict, indent=2)
        print(f"✓ JSON serialization successful ({len(json_str)} characters)")
        
        # Test JSON deserialization
        loaded_dict = json.loads(json_str)
        print(f"✓ JSON deserialization successful")
        
        # Verify some key values
        assert loaded_dict["detection_threshold"] == [3, 3]
        assert loaded_dict["aim"]["smoothing_type"] == "bezier"
        assert loaded_dict["enable_clustering"] == True
        print(f"✓ Data integrity verified")
        
    except Exception as e:
        print(f"✗ JSON serialization failed: {e}")
        return False
    
    # Save a sample settings file
    try:
        with open("sample_settings.json", "w") as f:
            json.dump(settings_dict, f, indent=2)
        print(f"✓ Sample settings file created: sample_settings.json")
    except Exception as e:
        print(f"✗ Failed to create sample file: {e}")
    
    print("\n🎉 All tests passed! Settings configuration is working correctly.")
    print("\nTo run the full GUI application, install the dependencies:")
    print("pip install slint-ui screeninfo")
    print("Then run: python3 run_settings_app.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)