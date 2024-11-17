import { Component, Input, OnInit } from '@angular/core';
import { DeviceService } from '../../services/devices.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-device-history',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './device-history.component.html',
  styleUrl: './device-history.component.css'
})
export class DeviceHistoryComponent implements OnInit {
  allDevicesHistory: any[] = [];  // Array to hold history of all devices

  constructor(private deviceService: DeviceService) { }

  ngOnInit(): void {
    // Fetch the history data for all devices
    this.deviceService.getAllDeviceHistory().subscribe(
      response => {
        // Assign the history for all devices from the response
        this.allDevicesHistory = response.devices;  // Should contain an array of devices with history
      },
      error => {
        console.error('Error fetching device history:', error);
      }
    );
  }
}