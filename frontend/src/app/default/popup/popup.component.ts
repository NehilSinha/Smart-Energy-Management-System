import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-popup',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './popup.component.html',
  styleUrl: './popup.component.css'
})
export class PopupComponent implements OnInit {
  isVisible: boolean = true;

  constructor() { }

  ngOnInit(): void {
    // Popup is visible when the page loads
  }

  // Method to close the popup
  closePopup(): void {
    this.isVisible = false;
    localStorage.setItem('popupClosed', 'true'); // Save state to prevent the popup from showing again
  }
}