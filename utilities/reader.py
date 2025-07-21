# reader.py
import json

class reader:

    def read(self, filename: str) -> dict:
        """Reads a JSON file
        
        :param string filename: The filepath to the JSON file.

        :return: The contents of the JSON file.
        :rtype: Dictionary.

        :raises FileNotFoundError: if the filename is not valid.
        :raises PermissionError: if the user doesn't have permission to read the file.
        :raises IOError: if there is  problem opening the file.
        :raises json.JSONDecodeError: if the JSON format is not correct.

        .. impl::
            :id: RDR_READ
            :implements: REQ001
            :tests: TTC001
        """
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Error: {filename} is not a valid file, or cannot be found. Please check the location. Traceback: {e} ")
        except PermissionError as e:
            print(f"Error: You do not have persmission to access this location or file. Traceback: {e} ")
        except IOError as e:
            print(f"Error: There was a problem loading the file. Traceback: {e} ")
        except json.JSONDecodeError as e:
            print(f"Error: There was a problem reading the JSON data. Traceback: {e} ")
        except Exception as e:
            print(f"Error: An unknown error has occured, please contact your system administrator. Traceback: {e} ")
