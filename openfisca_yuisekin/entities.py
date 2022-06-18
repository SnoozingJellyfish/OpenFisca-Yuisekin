"""
This file defines the entities needed by our legislation.

税金 and benefits can be calculated for different entities: persons, household, companies, etc.

See https://openfisca.org/doc/key-concepts/person,_entities,_role.html
"""

from openfisca_core.entities import build_entity

世帯 = build_entity(
    key = "household",
    plural = "households",
    label = "All the people in a family or group who live together in the same place.",
    doc = """
    世帯 is an example of a group entity.
    A group entity contains one or more individual·s.
    Each individual in a group entity has a role (e.g. parent or children). Some roles can only be held by a limited number of individuals (e.g. a 'first_parent' can only be held by one individual), while others can have an unlimited number of individuals (e.g. 'children').

    Example:
    Housing variables (e.g. 固定資産税') are usually defined for a group entity such as '世帯'.

    Usage:
    Check the number of individuals of a specific role (e.g. check if there is a 'second_parent' with household.nb_persons(世帯.SECOND_PARENT)).
    Calculate a variable applied to each individual of the group entity (e.g. calculate the '所得' of each member of the '世帯' with salaries = household.members("所得", period = MONTH); sum_salaries = household.sum(salaries)).

    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    """,
    roles = [
        {
            "key": "parent",
            "plural": "parents",
            "label": "Parents",
            "max": 2,
            "subroles": ["first_parent", "second_parent"],
            "doc": "The one or two adults in charge of the household.",
            },
        {
            "key": "child",
            "plural": "children",
            "label": "Child",
            "doc": "Other individuals living in the household.",
            },
        ],
    )

人物 = build_entity(
    key = "person",
    plural = "persons",
    label = "An individual. The minimal legal entity on which a legislation might be applied.",
    doc = """

    Variables like '所得' and '所得税' are usually defined for the entity '人物'.

    Usage:
    Calculate a variable applied to a '人物' (e.g. access the '所得' of a specific month with person("所得", "2017-05")).
    Check the role of a '人物' in a group entity (e.g. check if a the '人物' is a 'first_parent' in a '世帯' entity with person.has_role(世帯.FIRST_PARENT)).

    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    """,
    is_person = True,
    )

entities = [世帯, 人物]
