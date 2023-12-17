import os
import read_csv
from robot_context_manager import RobotContextManager


def robot_manager(robot_manager_obj: RobotContextManager) -> None:
    robot_manager_obj.open_base_url()
    robot_manager_obj.open_order_page()
    robot_orders_data = read_csv.CSV().read_csv_file()
    for row in robot_orders_data:
        robot_manager_obj.close_popup()
        robot_manager_obj.choose_head(row[1])
        robot_manager_obj.choose_body(row[2])
        robot_manager_obj.choose_legs(row[3])
        robot_manager_obj.enter_address(row[4])
        robot_manager_obj.open_preview()
        robot_manager_obj.make_robot_picture()
        robot_manager_obj.make_order()
        robot_manager_obj.rename_robot_pic()
        robot_manager_obj.add_pic_to_file()
        robot_manager_obj.another_robot()
    return None


if not os.path.exists('output'):
    os.makedirs('output')
else:
    for file in os.listdir('output'):
        os.remove(os.path.join('output', file))

with RobotContextManager() as robot:
    robot_manager(robot)
