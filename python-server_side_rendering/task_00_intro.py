#!/usr/bin/env python3
"""
Task 00: Creating a Simple Templating Program
Generates personalized invitation files from a template with placeholders.
"""

import logging
import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template using attendee data.

    Args:
        template (str): Template string with placeholders {name}, {event_title},
                       {event_date}, {event_location}
        attendees (list): List of dictionaries containing attendee information

    Returns:
        None: Creates output files or logs errors
    """
    # Configure logging
    logging.basicConfig(level=logging.ERROR, format='%(message)s')

    # Check input types
    if not isinstance(template, str):
        logging.error(f"Invalid input type: template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        logging.error(f"Invalid input type: attendees must be a list, got {type(attendees).__name__}")
        return

    # Check if all items in attendees are dictionaries
    if not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid input type: attendees must be a list of dictionaries")
        return

    # Check if template is empty
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template to work with
        personalized_template = template

        # Replace placeholders with values from attendee dictionary
        # Use .get() to handle missing keys and replace with "N/A"
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Handle None values explicitly
        if event_date is None:
            event_date = "N/A"
        if event_location is None:
            event_location = "N/A"

        # Replace placeholders in the template
        personalized_template = personalized_template.replace("{name}", str(name))
        personalized_template = personalized_template.replace("{event_title}", str(event_title))
        personalized_template = personalized_template.replace("{event_date}", str(event_date))
        personalized_template = personalized_template.replace("{event_location}", str(event_location))

        # Generate output filename
        output_filename = f"output_{index}.txt"

        # Write the processed template to output file
        try:
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(personalized_template)
        except IOError as e:
            logging.error(f"Error writing file {output_filename}: {e}")

