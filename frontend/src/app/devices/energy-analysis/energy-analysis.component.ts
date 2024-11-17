import { Component } from '@angular/core';
import { DeviceService } from '../../services/devices.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-energy-analysis',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './energy-analysis.component.html',
  styleUrl: './energy-analysis.component.css'
})
export class EnergyAnalysisComponent {
  analysisResults: any[] = [];

  constructor(private deviceService: DeviceService) { }

  analyzeAndTurnOff(): void {
    this.deviceService.analyzeAndTurnOff().subscribe(response => {
      this.analysisResults = response.results;
    });
  }
}
