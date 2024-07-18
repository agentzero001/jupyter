#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include "module.h"
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

#define numVAOs 1

GLuint renderingProgram;
GLuint vao[numVAOs];


GLuint createShaderProgram() {
    GLint vertCompiled;
    GLint fragCompiled;
    GLint linked; 

    //create empty shaders
    GLuint vShader = glCreateShader(GL_VERTEX_SHADER);
    GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);

    string vertShaderStr = readShaderSource("shaders/default.vert");
    string fragShaderStr = readShaderSource("shaders/default.frag");

    const char *vertShaderSrc = vertShaderStr.c_str();
    const char *fragShaderSrc = fragShaderStr.c_str();

    // //loads the GLSL code from the strings into the empty shader objects
    glShaderSource(vShader, 1, &vertShaderSrc, NULL);
    glShaderSource(fShader, 1, &fragShaderSrc, NULL);


    glCompileShader(vShader);
    CheckOpenGLError();
    glGetShaderiv(vShader, GL_COMPILE_STATUS, &vertCompiled);
    if (vertCompiled != 1) {
        cout << "vertex compilation failed" << endl;
        printShaderLog(vShader);
    }

    glCompileShader(fShader);
    CheckOpenGLError();
    glGetShaderiv(fShader, GL_COMPILE_STATUS, &fragCompiled);
    if (fragCompiled != 1) {
        cout << "fragment compilation failed" << endl;
        printShaderLog(fShader);
    }
    
    GLuint vfProgram = glCreateProgram();
    glAttachShader(vfProgram, vShader);
    glAttachShader(vfProgram, fShader);
    glLinkProgram(vfProgram);
    glGetProgramiv(vfProgram, GL_LINK_STATUS, &linked);
    if (linked != 1) {
        cout << "linking failed" << endl;
        printProgramLog(vfProgram);
    }

    return vfProgram;
}

void init(GLFWwindow* window) {
    renderingProgram = createShaderProgram();
    //When sets of data are prepared for sending down the pipeline, they are organized into buffers.
    //Those buffers are in turn organized into Vertex Array Objects.
    glGenVertexArrays(numVAOs, vao);
    glBindVertexArray(vao[0]);

}

void display(GLFWwindow* window, double currentTime) {
    glUseProgram(renderingProgram);
    glPointSize(30.0f);
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    glDrawArrays(GL_POINTS, 0, 1);
}

int main(void) {
    if (!glfwInit()) {exit(EXIT_FAILURE);}
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    GLFWwindow* window = glfwCreateWindow(600, 600, "program2", NULL, NULL);
    glfwMakeContextCurrent(window);
    if (glewInit() != GLEW_OK) {exit(EXIT_FAILURE);}
    glfwSwapInterval(1);
    init(window);

    while (!glfwWindowShouldClose(window)) {
        display(window, glfwGetTime());
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwDestroyWindow(window);
    glfwTerminate();
    exit(EXIT_SUCCESS);

}