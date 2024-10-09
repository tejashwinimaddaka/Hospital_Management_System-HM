class PropertyUtil:
    @staticmethod
    def getPropertyString(property_file_path=r"C:\Users\Asus\OneDrive\Desktop\HospitalManagement\util\properties.txt"):
        try:
            with open(property_file_path, 'r') as file:
                properties = {}
                for line in file:
                    key, value = line.strip().split('=')
                    properties[key.strip()] = value.strip()
                return properties
        except Exception as e:
            print(f"Error reading property file: {e}")
            return None