fun main() {
    println("Ingrese un número para la serie:")
    val n = readLine()!!.toInt()

    val serie = mutableListOf<Int>()
    for (i in 1..n) {
        repeat(i) {
            serie.add(i)
        }
    }

    println("Serie generada: ${serie.joinToString(", ")}")
}
