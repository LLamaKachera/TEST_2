fun main() {
    println("Ingrese un código donde el primer y último dígito sean iguales:")
    val codigo = readLine()!!.toInt()

    if (valida(codigo)) {
        val central = saca_central(codigo)
        muestra(central)
    } else {
        println("El primer y último dígito no son iguales.")
    }
}

fun valida(codigo: Int): Boolean {
    val codigoStr = codigo.toString()
    return codigoStr.first() == codigoStr.last()
}

fun saca_central(codigo: Int): String {
    val codigoStr = codigo.toString()
    return codigoStr.substring(1, codigoStr.length - 1)
}

fun muestra(central: String) {
    println("Parte central del código: $central")
}
