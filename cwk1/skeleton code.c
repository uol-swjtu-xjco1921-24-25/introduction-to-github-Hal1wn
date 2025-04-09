#include <stdio.h>   
#include <stdlib.h>  
#include <stdbool.h> 

#define MAX_SIZE 100    // 迷宫最大长宽
#define MIN_SIZE 5      // 迷宫最小长宽
#define WALL '#'        // 墙的符号
#define START 'S'       // 起点符号
#define EXIT 'E'        // 终点符号

typedef struct {
    char** grid;    // 迷宫地图
    int rows;       // 迷宫总行数
    int cols;       // 迷宫总列数
    struct {
        int x, y;           // 玩家当前位置
        int start_x, start_y; // 起点位置
        int exit_x, exit_y;   // 出口位置
    } position;
} Maze;


Maze* load_maze(const char* filename); //加载迷宫
/* 
    打开文件，检查是否成功
    创建迷宫对象
    读取迷宫尺寸和地图内容
    记录起点和出口位置 */


bool validate_dimensions(const Maze* maze); // 检查迷宫尺寸是否合法
/  - 行数/列数 >=5 且 <=100 */

bool is_valid_move(const Maze* maze, int x, int y); // 能否移动到指定位置
//  1. 不超出迷宫边界
//  2. 目标位置不是墙 

void move_player(Maze* maze, int dx, int dy); // 移动玩家
//  1. 计算新坐标
//  2. 用is_valid_move检查是否合法
//  3. 更新玩家位置或显示错误提示 

void render_maze(const Maze* maze); // 显示迷宫地图
//   - 玩家当前位置显示为X
//   - 起点S正常显示
//   - 每次显示前清空屏幕 

int main(int argc, char* argv[]) {
//流程：
//       1. 初始化：检查参数 -> 加载地图 -> 验证数据
//       2. 游戏循环：显示地图 -> 获取输入 -> 处理移动 -> 检查胜利
//          输入选项：
//          - W/A/S/D: 移动方向
//          - M/m: 显示地图（调用render_maze）
//          - Q/q: 退出游戏（直接结束循环）
//       3. 收尾工作：释放内存 -> 退出程序 */
    
    // 模拟输入处理逻辑
    char input;
    while (1) {
        // 获取输入
        scanf(" %c", &input);

        switch (tolower(input)) {
            case 'w': // 处理向上移动
                break;
            case 'a': // 处理向左移动
                break;
            case 's': // 处理向下移动
                break;
            case 'd': // 处理向右移动
                break;
            case 'm': // 输入"M/m"时调用render_maze显示地图
                break;
            case 'q': // 输入"Q/q"时退出游戏循环
                break;
            default: // 非法输入提示
                break;
        }
    }
}