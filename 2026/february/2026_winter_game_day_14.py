"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-19
                    2026 Winter Games Day 14: Ski Mountaineering
Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

The snow depth values are "Shallow", "Moderate", or "Deep".
Slope values are "Gentle", "Steep", or "Very Steep".
Return "Safe" or "Risky" based on this table:

                "Shallow"	"Moderate"	"Deep"
"Gentle"	    "Safe"	    "Safe"	    "Safe"
"Steep"	        "Safe"	    "Risky"	    "Risky"
"Very Steep"	"Safe"	"Risky"	    "Risky"
"""
def avalanche_risk(snow_depth, slope):
    risk_map = {
        ("Shallow", "Gentle"): "Safe",
        ("Shallow", "Steep"): "Safe",
        ("Shallow", "Very Steep"): "Safe",
        ("Moderate", "Gentle"): "Safe",
        ("Moderate", "Steep"): "Risky",
        ("Moderate", "Very Steep"): "Risky",
        ("Deep", "Gentle"): "Safe",
        ("Deep", "Steep"): "Risky",
        ("Deep", "Very Steep"): "Risky"
    }
    return risk_map[(snow_depth, slope)]

print(avalanche_risk("Shallow", "Gentle")    )    # should return "Safe".
print(avalanche_risk("Shallow", "Steep")     )    # should return "Safe".
print(avalanche_risk("Shallow", "Very Steep"))    # should return "Safe".
print(avalanche_risk("Moderate", "Gentle")   )    # should return "Safe".
print(avalanche_risk("Moderate", "Steep")    )    # should return "Risky".
print(avalanche_risk("Moderate", "Very Steep"))    # should return "Risky".
print(avalanche_risk("Deep", "Gentle")       )    # should return "Safe".
print(avalanche_risk("Deep", "Steep")        )    # should return "Risky".
