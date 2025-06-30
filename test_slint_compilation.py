#!/usr/bin/env python3
"""
Test script to verify Slint compilation works
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_simple_window():
    """Test loading a simple Slint window"""
    try:
        import slint
        
        # Test simple window first
        ui = slint.load_file('src/settings_app/ui/TestWindow.slint')
        print("✓ Simple test window compiled successfully")
        return True
        
    except ImportError:
        print("⚠ Slint module not available - install with: pip install slint-ui")
        return False
    except Exception as e:
        print(f"✗ Simple window compilation failed: {e}")
        return False

def test_components():
    """Test loading individual components"""
    try:
        import slint
        
        # Test components
        components = [
            'src/settings_app/ui/components/SliderGroup.slint',
            'src/settings_app/ui/components/CheckboxGroup.slint',
            'src/settings_app/ui/components/ComboBoxGroup.slint'
        ]
        
        for component in components:
            try:
                ui = slint.load_file(component)
                print(f"✓ {os.path.basename(component)} compiled successfully")
            except Exception as e:
                print(f"✗ {os.path.basename(component)} compilation failed: {e}")
                return False
        
        return True
        
    except ImportError:
        print("⚠ Slint module not available")
        return False

def test_views():
    """Test loading view components"""
    try:
        import slint
        
        include_paths = ['src/settings_app/ui']
        
        views = [
            'src/settings_app/ui/views/DetectionSettings.slint',
            'src/settings_app/ui/views/AimSettings.slint'
        ]
        
        for view in views:
            try:
                ui = slint.load_file(view, include_paths=include_paths)
                print(f"✓ {os.path.basename(view)} compiled successfully")
            except Exception as e:
                print(f"✗ {os.path.basename(view)} compilation failed: {e}")
                return False
        
        return True
        
    except ImportError:
        print("⚠ Slint module not available")
        return False

def test_main_window():
    """Test loading the main settings window"""
    try:
        import slint
        
        include_paths = ['src/settings_app/ui']
        
        try:
            ui = slint.load_file('src/settings_app/ui/SettingsWindow.slint', include_paths=include_paths)
            print("✓ SettingsWindow.slint compiled successfully")
            return True
        except Exception as e:
            print(f"✗ SettingsWindow.slint compilation failed: {e}")
            if hasattr(e, 'args') and len(e.args) > 1 and isinstance(e.args[1], list):
                print("Detailed diagnostics:")
                for i, diag in enumerate(e.args[1]):
                    print(f"  {i+1}. {diag}")
            return False
        
    except ImportError:
        print("⚠ Slint module not available")
        return False

def main():
    print("Testing Slint compilation...")
    print("=" * 50)
    
    success = True
    
    # Test in order of complexity
    if not test_simple_window():
        success = False
    
    if not test_components():
        success = False
    
    if not test_views():
        success = False
    
    if not test_main_window():
        success = False
    
    print("=" * 50)
    if success:
        print("🎉 All Slint files compiled successfully!")
        print("\nYou can now run the settings app with:")
        print("python3 run_settings_app.py")
    else:
        print("❌ Some Slint files failed to compile.")
        print("Please check the error messages above.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)