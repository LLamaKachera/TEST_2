fun main() {
    println("Ingrese un CI (al menos 4 dígitos mayores a 6):")
    val ci = readLine()!!.toInt()

    val digitoMayor = dig_mayor(ci)
    val digitoMenor = dig_menor(ci)

    println("Dígito mayor: $digitoMayor")
    println("Dígito menor: $digitoMenor")
}

fun dig_mayor(ci: Int): Int {
    var n = ci
    var mayor = 0
    while (n > 0) {
        val digito = n % 10
        if (digito > mayor) {
            mayor = digito
        }
        n /= 10
    }
    return mayor
}

fun dig_menor(ci: Int): Int {
    var n = ci
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
