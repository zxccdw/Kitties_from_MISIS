import { Input } from "../../components/Input/Input";

export default function RegistrationForm() {
  return (
    <form
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        width: "450px",
        marginBottom: "50px",
      }}
    >
      <div style={{ display: "flex", columnGap: "10px" }}>
        <div>
          <Input placeholder="Имя" alt="Name" type="text" />
        </div>
        <div>
          <Input placeholder="Фамилия" alt="Surname" type="text" />
        </div>
      </div>
      <Input placeholder="Дата " alt="Birthday" type="date" />
      <Input placeholder="Email" alt="Email" type="email" />
      <Input placeholder="Пароль" alt="Password" type="password" />
      <Input placeholder="Повторите пароль" alt="Password" type="password" />
      <input
        type="submit"
        value={"Зарегистрироваться"}
        style={{
          fontSize: "18px",
          padding: "5px 15px",
          marginTop: "20px",
          borderRadius: "10px",
          border: "2px solid red",
          color: "red",
          backgroundColor: "white",
          cursor: "pointer",
        }}
      />
    </form>
  );
}
