# parikshalab.in

Marketing site for ParikshaLab, a computer based test platform for NEET and JEE.
Plain static HTML, CSS and JavaScript. No build step.

## Files
- `index.html` single page site
- `styles.css` all styling (light theme)
- `script.js` scroll reveal, mobile menu, mockup countdown
- `CNAME` custom domain for GitHub Pages
- `.nojekyll` serves files as is

## Contact details in use
- WhatsApp and phone: +91 80881 58012 (`wa.me/918088158012`, `tel:+918088158012`)
- Email: admin.parikshalab@gmail.com

They appear in the three contact cards in `index.html` and in the floating WhatsApp
button at the bottom of the page. To change them later:

    sed -i 's/918088158012/91XXXXXXXXXX/g; s/+91 80881 58012/+91 XXXXX XXXXX/g' index.html
    sed -i 's/admin.parikshalab@gmail.com/your@address.in/g' index.html

The NEET section has a slot for the official notice. Wrap that line in a link to the
circular PDF once you have the URL.

## Publish on GitHub Pages
    git init
    git add .
    git commit -m "ParikshaLab site"
    git branch -M main
    git remote add origin https://github.com/manrayhod00/parikshalab-site.git
    git push -u origin main

Then in the repository, Settings, Pages, Source = Deploy from a branch, branch `main`,
folder `/ (root)`.

## Point parikshalab.in at GitHub
At your domain registrar add:

    A     @    185.199.108.153
    A     @    185.199.109.153
    A     @    185.199.110.153
    A     @    185.199.111.153
    CNAME www  manrayhod00.github.io.

Back in Settings, Pages, set the custom domain to `parikshalab.in` and tick
Enforce HTTPS once the certificate is issued.

## Local preview
    python3 -m http.server 8000
