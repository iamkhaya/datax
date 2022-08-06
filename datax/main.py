from typing import Dict, List
import csv
import logging

from datax.errors import InvalidConfigurationError, InvalidSourceFileError

def _validate_configuration(configuration) -> None:
    """
    Validate the configuration
    
    Args:
        configuration:
        
    Returns:
    
    Raises:
        InvalidConfigurationError:
        
    """
    try:
        print("validate the configuration")
        # 1. ensure configurations is type list of dicts
        # 2. ensure each dict contains valid keys
    except:
        raise InvalidConfigurationError("The configuration is invalid")
        
def _validate_source_file(source_file) -> None:
    """
    Validate the configuration
    
    Args:
        configuration:
        
    Returns:
    
    Raises:
        InvalidConfigurationError:
        
    """
    try:
        print("validate the configuration")
        # 1. ensure the file exists and is of type csv
        # 2. ensure the file contains the fields in the configuration
    except:
        raise InvalidSourceFileError("The source file is invalid")
        
def generate_mapped_file(configuration: List[Dict], source_file_name: str) -> Dict:
    """This method transforms the source csv file into the target 
    csv file with headings matching the configuration given.
    
    Args:
        configuration: A list of mapping pairs e.g
        source_file_name: the file path of the csv file to convert
        
    Returns:
        target_file_name: the file path of the target file
        
    Raises:
    """
    # validations
    _validate_configuration(configuration=configuration)
    _validate_source_file(source_file=source_file_name)

    # convert source file to target file
    with open(source_file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        
        # print(reader)
        fieldnames = ['Phone', 'Name', 'Surname']
        with open('target.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            new_file_rows = []
            for row in reader:
                logging.debug("source row : %s", row)
                
                record = {}
                for config in configuration:
                    print(f'config | field : {config["maps_to"]}, maps_to: {config["field"]}')
                    record[config["maps_to"]] = row[config["field"]]
                print('--- Record ---')
                print(record)
                logging.debug("target row : %s", record)
                writer.writerow(record)

                new_file_rows.append(record)
            
            print(new_file_rows)


if __name__ == "__main__":
    configuration: List[Dict] = [
        {
            "field": "phone",
            "maps_to": "Phone",
        },
        {
            "field": "first_name",
            "maps_to": "Name",
        },
        {
            "field": "last_name",
            "maps_to": "Surname",
        },
    ]
    generate_mapped_file(configuration=configuration, source_file_name='source.csv')
