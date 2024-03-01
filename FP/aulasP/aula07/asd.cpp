// Uma classe carros que tem um atributo privado chamado "velocidade" e um método público chamado "acelerar" que aumenta a velocidade em 10.

#include <iostream>
using namespace std;

class Carro {
    private:
        int velocidade;
    public:
        void acelerar() {
            velocidade += 10;
        }
        int getVelocidade() {
            return velocidade;
        }
    // COntrutor da classe
    Carro() {
        velocidade = 0;
    }

    // Memória dinâmica 

    for(int i = 0; i < 10; i++) {
        Carro *c = new Carro();
        delete c;
    }
    ~Carro() {
        cout << "Destrutor chamado" << endl;
    }
    
};
