"""
Settings Configuration App - A GUI for configuring detection and aim settings
"""
import os
import slint
import json
from screeninfo import get_monitors
from . import __path__

views_dir = os.path.join(__path__[0], "ui")

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
    ui = slint.load_file(os.path.join(views_dir, "SettingsWindow.slint"), include_paths=[views_dir])

    class SettingsApp(ui.SettingsWindow):
        def __init__(self):
            super().__init__()
            
            self.config = SettingsConfig()
            
            screen = [
                monitor
                for monitor in get_monitors()
                if monitor.is_primary
            ][0]
            self.size = slint.ListModel([1200, 800])
            self.maxSize = slint.ListModel([screen.width, screen.height])
            
            # Initialize UI with current values
            self._update_ui_from_config()

        def _update_ui_from_config(self):
            """Update UI elements with current configuration values"""
            # Detection settings
            self.set_detection_threshold_x(self.config.detection_threshold[0])
            self.set_detection_threshold_y(self.config.detection_threshold[1])
            self.set_upper_color_r(self.config.upper_color[0])
            self.set_upper_color_g(self.config.upper_color[1])
            self.set_upper_color_b(self.config.upper_color[2])
            self.set_lower_color_r(self.config.lower_color[0])
            self.set_lower_color_g(self.config.lower_color[1])
            self.set_lower_color_b(self.config.lower_color[2])
            self.set_min_contour_area(self.config.min_contour_area)
            self.set_density_threshold(self.config.density_threshold)
            self.set_enable_clustering(self.config.enable_clustering)
            self.set_cluster_distance(self.config.cluster_distance)
            self.set_min_cluster_size(self.config.min_cluster_size)
            self.set_max_cluster_size(self.config.max_cluster_size)
            self.set_fov_x(self.config.fov_x)
            self.set_fov_y(self.config.fov_y)
            self.set_aim_fov_x(self.config.aim_fov_x)
            self.set_aim_fov_y(self.config.aim_fov_y)
            self.set_fps(self.config.fps)
            self.set_auto_detect_resolution(self.config.auto_detect_resolution)
            self.set_resolution_x(self.config.resolution_x)
            self.set_resolution_y(self.config.resolution_y)
            
            # Aim settings
            self.set_aim_offset(self.config.aim_offset)
            self.set_aim_smooth(self.config.aim_smooth)
            self.set_aim_speed(self.config.aim_speed)
            self.set_aim_y_speed(self.config.aim_y_speed)
            self.set_aim_height(self.config.aim_height)
            self.set_smoothing_type(self.config.smoothing_type)
            self.set_ease_factor(self.config.ease_factor)
            self.set_min_ease_speed(self.config.min_ease_speed)
            self.set_bezier_control_offset(self.config.bezier_control_offset)
            self.set_bezier_tension(self.config.bezier_tension)
            self.set_movement_randomness(self.config.movement_randomness)
            self.set_deadzone(self.config.deadzone)
            
            # Anti-shake settings
            self.set_enable_anti_shake(self.config.enable_anti_shake)
            self.set_anti_shake_threshold(self.config.anti_shake_threshold)
            self.set_shake_suppression_factor(self.config.shake_suppression_factor)
            self.set_shake_escalation_threshold(self.config.shake_escalation_threshold)
            self.set_shake_escalation_rate(self.config.shake_escalation_rate)
            self.set_shake_cooldown_duration(self.config.shake_cooldown_duration)

        @slint.callback
        def save_settings_callback(self) -> str:
            """Save current settings to JSON file"""
            try:
                settings_dict = self.config.to_dict()
                with open("settings.json", "w") as f:
                    json.dump(settings_dict, f, indent=2)
                return "Settings saved successfully to settings.json"
            except Exception as e:
                return f"Error saving settings: {str(e)}"

        @slint.callback
        def load_settings_callback(self) -> str:
            """Load settings from JSON file"""
            try:
                with open("settings.json", "r") as f:
                    settings_dict = json.load(f)
                
                # Update config from loaded data
                if "detection_threshold" in settings_dict:
                    self.config.detection_threshold = settings_dict["detection_threshold"]
                if "upper_color" in settings_dict:
                    self.config.upper_color = settings_dict["upper_color"]
                if "lower_color" in settings_dict:
                    self.config.lower_color = settings_dict["lower_color"]
                
                # Update all other settings...
                for key, value in settings_dict.items():
                    if hasattr(self.config, key):
                        setattr(self.config, key, value)
                
                # Handle nested aim settings
                if "aim" in settings_dict:
                    aim_settings = settings_dict["aim"]
                    for key, value in aim_settings.items():
                        attr_name = f"aim_{key}" if not key.startswith("aim_") else key
                        if hasattr(self.config, attr_name):
                            setattr(self.config, attr_name, value)
                
                # Update UI with loaded values
                self._update_ui_from_config()
                
                return "Settings loaded successfully from settings.json"
            except FileNotFoundError:
                return "Settings file not found"
            except Exception as e:
                return f"Error loading settings: {str(e)}"

        @slint.callback
        def reset_to_defaults_callback(self):
            """Reset all settings to default values"""
            self.config = SettingsConfig()
            self._update_ui_from_config()

        # Detection threshold callbacks
        @slint.callback
        def detection_threshold_x_changed(self, value: int):
            self.config.detection_threshold[0] = value

        @slint.callback
        def detection_threshold_y_changed(self, value: int):
            self.config.detection_threshold[1] = value

        # Color callbacks
        @slint.callback
        def upper_color_r_changed(self, value: int):
            self.config.upper_color[0] = value

        @slint.callback
        def upper_color_g_changed(self, value: int):
            self.config.upper_color[1] = value

        @slint.callback
        def upper_color_b_changed(self, value: int):
            self.config.upper_color[2] = value

        @slint.callback
        def lower_color_r_changed(self, value: int):
            self.config.lower_color[0] = value

        @slint.callback
        def lower_color_g_changed(self, value: int):
            self.config.lower_color[1] = value

        @slint.callback
        def lower_color_b_changed(self, value: int):
            self.config.lower_color[2] = value

        # Other detection setting callbacks
        @slint.callback
        def min_contour_area_changed(self, value: int):
            self.config.min_contour_area = value

        @slint.callback
        def density_threshold_changed(self, value: float):
            self.config.density_threshold = value

        @slint.callback
        def enable_clustering_changed(self, value: bool):
            self.config.enable_clustering = value

        @slint.callback
        def cluster_distance_changed(self, value: int):
            self.config.cluster_distance = value

        @slint.callback
        def min_cluster_size_changed(self, value: int):
            self.config.min_cluster_size = value

        @slint.callback
        def max_cluster_size_changed(self, value: int):
            self.config.max_cluster_size = value

        @slint.callback
        def fov_x_changed(self, value: int):
            self.config.fov_x = value

        @slint.callback
        def fov_y_changed(self, value: int):
            self.config.fov_y = value

        @slint.callback
        def aim_fov_x_changed(self, value: int):
            self.config.aim_fov_x = value

        @slint.callback
        def aim_fov_y_changed(self, value: int):
            self.config.aim_fov_y = value

        @slint.callback
        def fps_changed(self, value: int):
            self.config.fps = value

        @slint.callback
        def auto_detect_resolution_changed(self, value: bool):
            self.config.auto_detect_resolution = value

        @slint.callback
        def resolution_x_changed(self, value: int):
            self.config.resolution_x = value

        @slint.callback
        def resolution_y_changed(self, value: int):
            self.config.resolution_y = value

        # Aim setting callbacks
        @slint.callback
        def aim_offset_changed(self, value: int):
            self.config.aim_offset = value

        @slint.callback
        def aim_smooth_changed(self, value: float):
            self.config.aim_smooth = value

        @slint.callback
        def aim_speed_changed(self, value: float):
            self.config.aim_speed = value

        @slint.callback
        def aim_y_speed_changed(self, value: float):
            self.config.aim_y_speed = value

        @slint.callback
        def aim_height_changed(self, value: float):
            self.config.aim_height = value

        @slint.callback
        def smoothing_type_changed(self, value: str):
            self.config.smoothing_type = value

        @slint.callback
        def ease_factor_changed(self, value: float):
            self.config.ease_factor = value

        @slint.callback
        def min_ease_speed_changed(self, value: float):
            self.config.min_ease_speed = value

        @slint.callback
        def bezier_control_offset_changed(self, value: float):
            self.config.bezier_control_offset = value

        @slint.callback
        def bezier_tension_changed(self, value: float):
            self.config.bezier_tension = value

        @slint.callback
        def movement_randomness_changed(self, value: float):
            self.config.movement_randomness = value

        @slint.callback
        def deadzone_changed(self, value: int):
            self.config.deadzone = value

        # Anti-shake setting callbacks
        @slint.callback
        def enable_anti_shake_changed(self, value: bool):
            self.config.enable_anti_shake = value

        @slint.callback
        def anti_shake_threshold_changed(self, value: float):
            self.config.anti_shake_threshold = value

        @slint.callback
        def shake_suppression_factor_changed(self, value: float):
            self.config.shake_suppression_factor = value

        @slint.callback
        def shake_escalation_threshold_changed(self, value: float):
            self.config.shake_escalation_threshold = value

        @slint.callback
        def shake_escalation_rate_changed(self, value: float):
            self.config.shake_escalation_rate = value

        @slint.callback
        def shake_cooldown_duration_changed(self, value: float):
            self.config.shake_cooldown_duration = value

    app = SettingsApp()
    app.run()