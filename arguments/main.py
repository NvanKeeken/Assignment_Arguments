# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1 : Greet Template


def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace("<name>", name)

# part 2 : Force
# function force returns result of formula force = mass * gravity


def force(mass, body="earth"):
    force = 0
    gravity_factors_per_body = {"mercury": 3.7, "venus": 8.9, "earth": 9.8,
                                "moon": 1.6, "mars": 3.7, "jupiter": 24.8,
                                "saturn": 10.4, "uranus": 8.9, "neptune": 11.2,
                                "pluto": 0.6, "sun": 274.0}
    if body in gravity_factors_per_body:
        force = mass * gravity_factors_per_body[body]
    return force

# Part 3 : Gravity
# function pull returns result of formula pull = g((m1*m2)/d2)


def pull(m1, m2, d):
    gravitational_constant = 6.674 * 10**-11
    pull = gravitational_constant * ((m1 * m2)/d**2)
    return pull
