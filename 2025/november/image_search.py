"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-04

                                        Image Search
On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

Ignore the case when matching the search terms.
Return the images in the same order they appear in the input array.
"""
def image_search(images, term):
    search_output = []

    for image in images:
        if term.lower() in image.lower():
            search_output.append(image)
    return search_output 

# Time complexity: O(n * m) n is number of images name, m is average length of image name in array