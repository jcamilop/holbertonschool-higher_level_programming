import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io
from io import StringIO


class TestRectangle(unittest.TestCase):
    
    def test_rectangle_initialization(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def test_valid_width_height(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
    def test_valid_width_height_x(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
    def test_valid_width_height_x_y(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_invalid_width_value(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
    def test_invalid_height_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
    def test_invalid_x_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
    def test_invalid_x_negative_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
    def test_invalid_y_negative_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)
    def test_str(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")

    def test_to_dictionary(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_update(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9, 10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)

    def test_update_args_width_height(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_update_args_width_height_x(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 4)
    def test_update_args_width_height_x_y(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9, 10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)
    def test_update_kwargs(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_update_kwargs_width_height(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6, 'width': 7, 'height': 8})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_update_kwargs_width_height_x(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6, 'width': 7, 'height': 8, 'x': 9})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 4)
    def test_update_kwargs_width_height_x_y(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)
        
    def test_rectangle_height_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_rectangle_x_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -1)

    def test_rectangle_y_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 0, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 0, -1)
            

    def test_rectangle_str(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(rect), expected_output)

    
    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)
            
    def test_display(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        expected_output = "\n\n\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
            
    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)
    
    def test_rectangle_display_without_x_y(self):
        rectangle = Rectangle(5, 3)
        expected_output = "#####\n#####\n#####\n"
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_display_without_y(self):
        rectangle = Rectangle(5, 3, 2)
        expected_output = "  #####\n  #####\n  #####\n"
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    
    def test_rectangle_update_with_args(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(2, 6, 7, 1, 4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_with_kwargs(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(id=2, width=6, height=7, x=1, y=4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 4)
        
        def test_rectangle_update_with_kwargs(self):
            rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(id=2, width=6, height=7, x=1, y=4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 4)



    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {
            "x": 2,
            "y": 3,
            "id": 1,
            "height": 10,
            "width": 5
        }
        self.assertDictEqual(rect_dict, expected_dict)
        


if __name__ == '__main__':
    unittest.main()
