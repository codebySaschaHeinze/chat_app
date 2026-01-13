import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Chat {
  id: number;
  name: string;
  message: string;
  created_at: string;
}

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.html',
})
export class App implements OnInit {
  chats: Chat[] = [];

  constructor(private http: HttpClient) {}

  name = '';
  message = '';

  ngOnInit(): void {
    this.loadChats();
  }

  loadChats(): void {
    this.http.get<Chat[]>('/api/chat/').subscribe((data) => {
      this.chats = data;
    });
  }

  onNameChange(value: string) {
    this.name = value;
  }

  onMessageChange(value: string) {
    this.message = value;
  }

  sendMessage(): void {
    const name = this.name.trim();
    const message = this.message.trim();

    if (!name || !message) return;

    this.http.post<Chat>('/api/chat/', { name, message }).subscribe((created) => {
      this.chats = [created, ...this.chats];
      this.name = '';
      this.message = '';
    });
  }
}
