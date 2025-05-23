import "dotenv/config";
import "./config/auth";
import app from "./app";
import "./config/db";

const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
  console.log(`server listening on ${PORT}`);
});
