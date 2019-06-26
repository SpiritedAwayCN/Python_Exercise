@echo off

cd ./World_of_Warcraft1
echo Running ./World_of_Warcraft1/main.py
main.py > data/my_output.txt
cd ./data
fc my_output.txt std_output.txt
cd ../../

cd ./World_of_Warcraft2
echo Running ./World_of_Warcraft2/main.py
main.py > data/my_output.txt
cd ./data
fc my_output.txt std_output.txt
cd ../../

cd ./World_of_Warcraft3
echo Running ./World_of_Warcraft3/main.py
main.py > data/my_output.txt
cd ./data
fc my_output.txt std_output.txt
cd ../../

cd ./World_of_WarcraftFinal
echo Running ./World_of_WarcraftFinal/main.py
main.py > data/my_output.txt
cd ./data
fc my_output.txt std_output.txt
cd ../../

pause