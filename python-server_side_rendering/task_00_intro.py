import os
import logging

# Set up logging configuration
logging.basicConfig(level=logging.ERROR, format='%(message)s')

def generate_invitations(template, attendees):
    # Check if the template is a string and the attendees is a list of dictionaries
    if not isinstance(template, str):
        logging.error("Invalid input type: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input type: attendees should be a list of dictionaries.")
        return

    # Check if the template is empty
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Check if the list of attendees is empty
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee-specific data
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A')
        event_date = attendee.get('event_date', 'N/A') if attendee.get('event_date') else 'N/A'
        event_location = attendee.get('event_location', 'N/A')

        # Create the personalized invitation
        personalized_invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        # Generate the file name
        file_name = f'output_{index}.txt'

        # Write the personalized invitation to the file
        try:
            with open(file_name, 'w') as file:
                file.write(personalized_invitation)
        except IOError as e:
            logging.error(f"Error writing file {file_name}: {e}")

