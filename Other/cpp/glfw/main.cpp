#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream>

using namespace std;

#define numVAOs 1

GLuint renderingProgram;
GLuint vao[numVAOs];


GLuint createShaderProgram() {

    //the primary purpose of any vertex shader is to send a vertex down the pipeline
    //the vertices move through the pipeline to the rasterizer,
    //where they are transformed into pixel locations (or fragments)
    const char *vshaderSource = 
        "#version 430 \n"
        "void main(void) \n"
        "{gl_Position = vec4(0.0, 0.0, 0.0, 1.0);}";

    //Eventually these pixels (fragments) reach the fragment shader.
    //The purpose of any fragment shader is to set the RGB (RGBa) color of a pixel to be displayed.
    const char *fshaderSource = 
        "#version 430 \n"
        "out vec4 color; \n"
        "void main (void) \n"
        "{color = vec4(0.0, 0.0, 1.0, 1.0);}";

    //create empty shaders
    GLuint vShader = glCreateShader(GL_VERTEX_SHADER);
    GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);

    //loads the GLSL code from the strings into the empty shader objects
    glShaderSource(vShader, 1, &vshaderSource, NULL);
    glShaderSource(fShader, 1, &fshaderSource, NULL);

    glCompileShader(vShader);
    glCompileShader(fShader);

    GLuint vfProgram = glCreateProgram();
    glAttachShader(vfProgram, vShader);
    glAttachShader(vfProgram, fShader);
    glLinkProgram(vfProgram);

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