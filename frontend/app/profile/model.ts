export interface Profile {
  id_user: number;
  first_name: string;
  last_name: string;
  third_name?: string;
  email: string;
  date_of_birth?: string;
  sex: "M" | "W";
  phoneNumber: string;
  fan_status?: "base" | "cool" | "champion" | "legend";
  avatarURL?: string;
  is_staff: boolean;
}

export interface GameEvent {
  id_event: number;
  title: string;
  description: string;
  end_date?: string;
  people_limit?: number;
  location?: string;
  stream_url?: string;
}
