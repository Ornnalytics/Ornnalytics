/*console.log("Importing mysql")
import mysql from 'mysql2';
console.log("Imported mysql")
const con = mysql.createConnection({
    host: "localhost",
    user: "LeagueOfLegends",
    password: "@Peacer9811", 
    database: "league_of_legends"
});


console.log("Created var con")

var mySQLFunctions = {
    getChamps() {
        let _result;
        con.connect(function(err) {
        if (err) throw err;
        console.log("Connected!");
        con.query("SELECT * FROM champ", function (err, result) {
          if (err) throw err;
          _result = result;
        });
      })
      return _result;
    }
}

export default mySQLFunctions
*/