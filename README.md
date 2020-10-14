# Openai-ROS Robotic_Arm
Final Master Thesis Project. 
This project has as final goal make use of RL platforms to train custom, low-cost robot with the aim of developing a usefull and aforable tool that could be applied for numerous applications.

# Fetch Robot Training with Openai-ROS
In this repository we provide the environment that serves as interface for ROS and OpenaAI Gym, contretely for the Fetch Robot. But with the corresponding adjusment this environments can be employed in generic robotic arms. To employ these files they just need to be placed inside the package openai_ros of your catkin directory and also you should have the pacakage for generating the Fetch model in Gazebo before executing the training. To begin the training the training scripts must be placed inside the corresponding baselines packages, inside the HER folder. 
Currently non of the basalines algorithm are working with this setup.
Video demo: https://www.youtube.com/watch?v=myYmVcTtJbg&ab_channel=MarioAceraMarioAcera

# Moveo Robot in Gazebo
We also provide a functional Gazebo model for the Moveo Robot but with no end-effector that should be adapted and remodeled. The Gazebo model also has it associated Moveit package and the controllers interface is properly built, so the simulated model can be controlled through the Moveit API. Having a functional robot model is the foundation for using Openai-ROS package.
Video demo: https://www.youtube.com/watch?v=P8Ep4FNqFCE&ab_channel=MarioAceraMarioAcera
