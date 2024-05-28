import 'dart:io';
import 'package:sqflite_common/sqlite_api.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';

class DatabaseHelper {
  static Database? _database;

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await initDB();
    return _database!;
  }

  initDB() async {
    sqfliteFfiInit(); // Initialize sqflite_ffi
    var databaseFactory = databaseFactoryFfi; // Use the FFI factory
    var documentsDirectory = await getApplicationDocumentsDirectory();
    String path = join(documentsDirectory.path, "RecipesDB.db");
    return await databaseFactory.openDatabase(path, options: OpenDatabaseOptions(
      version: 1,
      onCreate: (Database db, int version) async {
        await db.execute(
          "CREATE TABLE Recipes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)",
        );
      },
    ));
  }

  Future<void> insertRecipe(String title, String content) async {
    final db = await database;
    await db.insert(
      'Recipes',
      {'title': title, 'content': content},
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<List<Map<String, dynamic>>> getRecipes() async {
    final db = await database;
    return await db.query("Recipes");
  }
}