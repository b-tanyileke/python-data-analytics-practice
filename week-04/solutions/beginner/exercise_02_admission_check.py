"""Exercise 2 sample solution."""


def admission_message(age, ticket_response):
    """ returns a string based on the age and ticket response """
    if age >= 18 and ticket_response == "yes":
        return "Admitted"
    return "Not admitted"
