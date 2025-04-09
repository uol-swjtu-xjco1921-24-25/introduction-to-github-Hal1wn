import unittest
import subprocess
import os

class TestMazeGame(unittest.TestCase):
    def setUp(self):
        # 定义测试迷宫文件路径
        self.maze_files = {
            # 合法迷宫
            "simple": os.path.join("test_data", "valid", "maze1.txt"),
            "complex": os.path.join("test_data", "valid", "maze2.txt"),
            # 非法迷宫
            "too_large": os.path.join("test_data", "invalid", "too_large.txt"),
            "too_small": os.path.join("test_data", "invalid", "too_small.txt"),
        }

    def test_simple_maze(self):
        """测试简单迷宫正常通关"""
        input_sequence = "d\nd\ns\n"
        result = subprocess.run(
            ["./maze", self.maze_files["simple"]],
            input=input_sequence,
            text=True,
            capture_output=True
        )
        self.assertIn("Congratulations! You escaped!", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test_complex_maze(self):
        """测试复杂迷宫正常通关"""
        input_sequence = "d\ns\ns\nd\nd\nw\na\ns\ns\ns\nd\nd\n"
        result = subprocess.run(
            ["./maze", self.maze_files["complex"]],
            input=input_sequence,
            text=True,
            capture_output=True
        )
        self.assertIn("Congratulations! You escaped!", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test_case_insensitive_input(self):
        """测试大小写混合输入（W/a/S）"""
        input_sequence = "W\na\nS\nq\n"
        result = subprocess.run(
            ["./maze", self.maze_files["simple"]],
            input=input_sequence,
            text=True,
            capture_output=True
        )
        self.assertEqual(result.stdout.count("Moved to"), 3)
        self.assertIn("Invalid input", result.stdout)

    def test_boundary_movement(self):
        """测试玩家移动到地图外（使用复杂迷宫）"""
        input_sequence = "a\na\na\nq\n"  # 强制向左越界
        result = subprocess.run(
            ["./maze", self.maze_files["complex"]],
            input=input_sequence,
            text=True,
            capture_output=True
        )
        self.assertIn("out of bounds", result.stdout.lower())
        self.assertLess(result.stdout.count("Moved to"), 3)

    def test_map_command(self):
        """测试M键显示地图功能"""
        input_sequence = "m\nd\nm\nq\n"
        result = subprocess.run(
            ["./maze", self.maze_files["simple"]],
            input=input_sequence,
            text=True,
            capture_output=True
        )
        self.assertEqual(result.stdout.count("X"), 3)

    def test_quit_functionality(self):
        """测试Q键退出功能"""
        input_sequence = "d\nq\n"
        result = subprocess.run(
            ["./maze", self.maze_files["simple"]],
            input=input_sequence,
            text=True,
            capture_output=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Exiting", result.stdout)
        self.assertIn("Moved to", result.stdout)

    def test_invalid_maze_too_large(self):
        """测试过大迷宫文件加载失败"""
        result = subprocess.run(
            ["./maze", self.maze_files["too_large"]],
            text=True,
            capture_output=True
        )
        self.assertIn("Invalid maze configuration", result.stdout)
        self.assertNotEqual(result.returncode, 0)

    def test_invalid_maze_too_small(self):
        """测试过小迷宫文件加载失败"""
        result = subprocess.run(
            ["./maze", self.maze_files["too_small"]],
            text=True,
            capture_output=True
        )
        self.assertIn("Invalid maze configuration", result.stdout)
        self.assertNotEqual(result.returncode, 0)

if __name__ == "__main__":
    unittest.main()