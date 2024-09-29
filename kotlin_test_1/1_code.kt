fun main() {
    println("Ingrese 4 números separados por espacios:")
    val numeros = readLine()!!.split(" ").map { it.toInt() }.toMutableList()
    numeros.sort()
    println("Números ordenados: ${numeros.joinToString(", ")}")
}
