export interface Profile {
  id: string;
  avatarURL: string;
  firstName: string;
  lastName: string;
  thirdName: string;
  birhday: string;
  phoneNumber: string;
  sex: "M" | "W";
  fanStatus: "base" | "cool" | "champion" | "legend";
  email: string;
  role: "fan" | "coach" | "player";
  matches: string[];
}
