fun main() {
    println("Ingrese un código de 5 dígitos:")
    val codigo = readLine()!!.toInt()

    val invertido = invierte(codigo)
    muestra(invertido)
}

fun invierte(numero: Int): Int {
    var n = numero
    var invertido = 0
    while (n > 0) {
        val digito = mod(n, 10)
        invertido = invertido * 10 + digito
        n /= 10
    }
    return invertido
}

fun mod(a: Int, b: Int): Int {
    return a % b
}

fun muestra(valor: Int) {
    println("El número invertido es: $valor")
}
