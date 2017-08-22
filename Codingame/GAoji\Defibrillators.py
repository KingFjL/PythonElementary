import math._
import scala.util._

object Geo {

    def dist(lat1:String, lon1:String, lat2:String, lon2:String):Double = {

        val la1 = lat1.replace(",", ".").toDouble.toRadians;
        val lo1 = lon1.replace(",", ".").toDouble.toRadians;
        val la2 = lat2.replace(",", ".").toDouble.toRadians;
        val lo2 = lon2.replace(",", ".").toDouble.toRadians;

        val x = (lo2 - lo1) * cos((la1 + la2) / 2);
        val y = (la2 - la1);

        return sqrt(x * x + y * y) * 6371;
    }
}

object Solution extends App {

    var minName:String = ""
    var minDist:Double = 10000000000.0

    val lon = readLine
    val lat = readLine
    val n   = readInt

    for(i <- 0 until n) {
        val defib = readLine

        val e = defib.split(";")
        val d = Geo.dist(lat, lon, e(5), e(4))

        if (minDist > d) {
            minDist = d
            minName = e(1)
        }
    }
    println(minName)
}
