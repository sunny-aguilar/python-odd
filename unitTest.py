
import unittest

def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()


print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")



class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('sandro', 'aguilar')
        self.assertEqual(formatted_name, 'Sandro Aguilar')

if __name__ == '__main__':
    unittest.main()


