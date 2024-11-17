import { Component, OnInit } from '@angular/core';
import { DeviceService } from '../../services/devices.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-device-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './device-list.component.html',
  styleUrl: './device-list.component.css'
})
export class DeviceListComponent implements OnInit {
  devices: any[] = [];

  constructor(private deviceService: DeviceService) { }

  ngOnInit(): void {
    this.deviceService.getDevices().subscribe(response => {
      this.devices = response.devices;
    });
  }

  toggleDevice(id: number): void {
    this.deviceService.toggleDevice(id).subscribe(() => {
      this.ngOnInit(); // Refresh the device list
    });
  }
  
}
