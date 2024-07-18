#include "module.h"
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>


using namespace std;


void printShaderLog(GLuint shader){
    int len = 0;
    int chWrittn = 0;
    char *log;
    glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &len);
    if (len > 0) {
        log = (char *)malloc(len);
        glGetShaderInfoLog(shader, len, &chWrittn, log);
        cout << "Shader Info Log:" << log << endl;
        free(log);
    }
}

void printProgramLog(int prog) {
    int len = 0;
    int chWrittn = 0;
    char *log;
    glGetProgramiv(prog, GL_INFO_LOG_LENGTH, &len);
    if (len > 0) {
        log = (char *)malloc(len);
        glGetShaderInfoLog(prog, len, &chWrittn, log);
        cout << "Program Info Log:" << log << endl;
        free(log);
    }
}


bool CheckOpenGLError() {
    bool foundError = false;
    int glErr = glGetError();
    while (glErr != GL_NO_ERROR) {
        cout << "glError:" << glErr << endl;
        foundError = true;
        glErr = glGetError();
    }
    return foundError;
}


string readShaderSource(const char *filePath) {
    string content;
    ifstream fileStream(filePath, ios::in);
    string line = "";
    while (!fileStream.eof()) {
        getline(fileStream, line);
        content.append(line + "\n");
    }
    fileStream.close();
    return content;
}
