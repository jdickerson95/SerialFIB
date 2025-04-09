class MockSEM:
    """Mock implementation of Zeiss SEM_API class"""
    
    def __init__(self):
        self.beam_blanker = False
        self.beam_current = 1.0
        self.stage_position = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'r': 0.0, 't': 0.0}
        self.magnification = 1000
        self.detector = "SE"
        self.working_distance = 10.0
        self.scanning = False
        self.image_width = 1024
        self.image_height = 768
        self.initialized = True
        self.connected = True
        self.output_dir = "/tmp/mock_sem_output"
        print("Mock SEM_API initialized")
        
    def initialise(self):
        self.initialized = True
        return True
        
    def connect(self):
        self.connected = True
        return True
        
    def disconnect(self):
        self.connected = False
        return True
        
    def blank_beam(self, state=True):
        self.beam_blanker = state
        return True
        
    def get_beam_blanker_state(self):
        return self.beam_blanker
        
    def set_beam_current(self, current):
        self.beam_current = current
        return True
        
    def get_beam_current(self):
        return self.beam_current
        
    def set_stage_position(self, x=None, y=None, z=None, r=None, t=None):
        if x is not None:
            self.stage_position['x'] = x
        if y is not None:
            self.stage_position['y'] = y
        if z is not None:
            self.stage_position['z'] = z
        if r is not None:
            self.stage_position['r'] = r
        if t is not None:
            self.stage_position['t'] = t
        return True
        
    def get_stage_position(self):
        return self.stage_position
        
    def set_magnification(self, mag):
        self.magnification = mag
        return True
        
    def get_magnification(self):
        return self.magnification
        
    def acquire_image(self):
        import numpy as np
        # Return a mock image with random noise
        return np.random.randint(0, 255, (self.image_height, self.image_width), dtype=np.uint8)

    def define_output_dir(self, directory):
        """Set the output directory for saved images and data"""
        print(f"Mock SEM: Setting output directory to {directory}")
        self.output_dir = directory
        # Create directory if it doesn't exist
        import os
        if not os.path.exists(directory):
            os.makedirs(directory)
        return True
    
    # Additional methods that might be needed based on your code
    def get_output_dir(self):
        """Get the current output directory"""
        return self.output_dir
    
    def save_image(self, filename, image=None):
        """Mock saving an image to the output directory"""
        import os
        import numpy as np
        from PIL import Image
        
        filepath = os.path.join(self.output_dir, filename)
        print(f"Mock SEM: Saving image to {filepath}")
        
        # If no image provided, generate a mock one
        if image is None:
            image = self.acquire_image()
        
        # Save the image
        img = Image.fromarray(image)
        img.save(filepath)
        return filepath
    
    def set_detector(self, detector):
        """Set the active detector"""
        print(f"Mock SEM: Setting detector to {detector}")
        self.detector = detector
        return True
    
    def get_detector(self):
        """Get the active detector"""
        return self.detector
    
    def set_working_distance(self, wd):
        """Set the working distance"""
        print(f"Mock SEM: Setting working distance to {wd}")
        self.working_distance = wd
        return True
    
    def get_working_distance(self):
        """Get the working distance"""
        return self.working_distance
    
    def start_scanning(self):
        """Start continuous scanning"""
        print("Mock SEM: Starting continuous scanning")
        self.scanning = True
        return True
    
    def stop_scanning(self):
        """Stop continuous scanning"""
        print("Mock SEM: Stopping continuous scanning")
        self.scanning = False
        return True
    
    def is_scanning(self):
        """Check if scanning is active"""
        return self.scanning
    
    def set_scan_resolution(self, width, height):
        """Set the scan resolution"""
        print(f"Mock SEM: Setting scan resolution to {width}x{height}")
        self.image_width = width
        self.image_height = height
        return True
    
    def get_scan_resolution(self):
        """Get the current scan resolution"""
        return (self.image_width, self.image_height)
        
    def get_microscope_state(self):
        """Get the overall microscope state"""
        return {
            "beam_blanker": self.beam_blanker,
            "beam_current": self.beam_current,
            "stage_position": self.stage_position,
            "magnification": self.magnification,
            "detector": self.detector,
            "working_distance": self.working_distance,
            "scanning": self.scanning,
            "resolution": (self.image_width, self.image_height),
            "output_dir": self.output_dir
        }
    
    # Add a catch-all method to handle unexpected method calls during testing
    def __getattr__(self, name):
        def method(*args, **kwargs):
            arg_str = ', '.join([str(a) for a in args] + [f"{k}={v}" for k, v in kwargs.items()])
            print(f"WARNING: Called undefined mock method: {name}({arg_str})")
            return True  # Return a reasonable default
        return method

    # Add any other methods that are called in your code 