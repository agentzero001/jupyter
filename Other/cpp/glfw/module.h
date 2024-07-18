#ifndef SHADER_UTILS_H
#define SHADER_UTILS_H
#include <GL/glew.h>  
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>



void printShaderLog(GLuint shader);
void printProgramLog(int prog);
bool CheckOpenGLError();
std::string readShaderSource(const char *filePath);

#endif 