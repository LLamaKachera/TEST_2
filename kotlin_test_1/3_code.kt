fun esCapicua(numero: Int): Boolean {
    val numeroString = numero.toString()
    return numeroString == numeroString.reversed()
}

fun main() {
    val capicuas = mutableListOf<Int>()
    var num = 0

    while (capicuas.size < 20) {
        if (esCapicua(num)) {
            capicuas.add(num)
        }
        num++
    }

    println("Los 20 primeros números capicúas son: ${capicuas.joinToString(", ")}")
}
