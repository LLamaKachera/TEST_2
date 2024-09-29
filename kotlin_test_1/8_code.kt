fun main() {
    println("Ingrese una nota final:")
    val nota = readLine()!!.toInt()

    val digitoMenor = dig_menor(nota)
    val factorial = factorial(digitoMenor)

    muestra(factorial)
}

fun dig_menor(numero: Int): Int {
    var n = numero
    var menor = 9
    while (n > 0) {
        val digito = n % 10
        if (digito < menor) {
            menor = digito
        }
        n /= 10
    }
    return menor
}

fun factorial(n: Int): Int {
    return if (n <= 1) 1 else n * factorial(n - 1)
}

fun muestra(valor: Int) {
    println("Factorial del dígito menor: $valor")
}
