import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DeviceService {
  private apiUrl = 'http://127.0.0.1:5000/api'; // Replace with your Flask backend URL

  constructor(private http: HttpClient) { }

  // Get all devices
  getDevices(): Observable<any> {
    return this.http.get(`${this.apiUrl}/devices`);
  }

  // Toggle device (turn on/off)
  toggleDevice(deviceId: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/device/${deviceId}/toggle`, {});
  }

  // Get all device history (updated to use GET request)
  getAllDeviceHistory(): Observable<any> {
    return this.http.get(`${this.apiUrl}/device/history`);  // Change POST to GET
  }

  // Analyze and turn off idle devices
  analyzeAndTurnOff(): Observable<any> {
    return this.http.post(`${this.apiUrl}/analyze-and-turn-off`, {});
  }
}
