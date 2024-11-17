import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { DeviceListComponent } from "./devices/device-list/device-list.component";
import { EnergyAnalysisComponent } from "./devices/energy-analysis/energy-analysis.component";
import { DeviceHistoryComponent } from "./devices/device-history/device-history.component";
import { HeaderComponent } from "./default/header/header.component";
import { FooterComponent } from "./default/footer/footer.component";
import { PopupComponent } from "./default/popup/popup.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, DeviceListComponent, EnergyAnalysisComponent, DeviceHistoryComponent, HeaderComponent, FooterComponent, PopupComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Energy Investigation';
}
